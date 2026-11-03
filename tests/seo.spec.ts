/**
 * seo.spec.ts
 *
 * Validates search engines related markup:
 * - a single h1 per page, the slogan on the home page
 * - reciprocal hreflang alternates between EN and FR pages, with an x-default
 * - a meta description on every page, and distinct titles and descriptions on the posts list pages
 */

import { test, expect } from '@playwright/test';

// EN and FR versions of the same pages
const pairs = [
  { en: '/', fr: '/fr/' },
  { en: '/about/', fr: '/fr/a-propos/' },
  { en: '/contribute/', fr: '/fr/contribuer/' },
  { en: '/contact/', fr: '/fr/contact/' },
];

test.describe('Headings', () => {
  for (const [url, slogan] of [['/', 'Free your association management!'], ['/fr/', 'Libérez la gestion de votre association !']]) {
    test(`[seo] ${url} - slogan is the only h1`, async ({ page }) => {
      await page.goto(url);
      await expect(page.locator('h1')).toHaveCount(1);
      await expect(page.locator('h1')).toHaveText(slogan);
    });
  }

  for (const pair of pairs.slice(1)) {
    for (const url of [pair.en, pair.fr]) {
      test(`[seo] ${url} - single h1`, async ({ page }) => {
        await page.goto(url);
        await expect(page.locator('h1')).toHaveCount(1);
      });
    }
  }
});

test.describe('hreflang', () => {
  for (const pair of pairs) {
    for (const url of [pair.en, pair.fr]) {
      test(`[seo] ${url} - alternates`, async ({ page }) => {
        await page.goto(url);

        const href = async (lang: string) =>
          new URL((await page.locator(`link[rel="alternate"][hreflang="${lang}"]`).getAttribute('href'))!).pathname;

        expect(await href('en')).toBe(pair.en);
        expect(await href('fr')).toBe(pair.fr);
        expect(await href('x-default')).toBe(pair.en);
      });
    }
  }
});

test.describe('Descriptions', () => {
  // A page without description in its front matter gets the beginning of its content
  for (const url of [...pairs.flatMap((pair) => [pair.en, pair.fr]), '/posts/', '/post/2026/11/03/galette-1-3-2/']) {
    test(`[seo] ${url} - meta description`, async ({ page }) => {
      await page.goto(url);
      const description = await page.locator('meta[name="description"]').getAttribute('content');
      expect(description!.length).toBeGreaterThan(70);
      expect(await page.locator('meta[property="og:description"]').getAttribute('content')).toBe(description);
    });
  }

  test('[seo] posts list pages - distinct title and description', async ({ page }) => {
    await page.goto('/posts/');
    const title = await page.title();
    const description = await page.locator('meta[name="description"]').getAttribute('content');

    await page.goto('/posts/page/2/');
    expect(await page.title()).not.toBe(title);
    expect(await page.locator('meta[name="description"]').getAttribute('content')).not.toBe(description);
  });
});
