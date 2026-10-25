/**
 * seo.spec.ts
 *
 * Validates search engines related markup:
 * - a single h1 per page, the slogan on the home page
 * - reciprocal hreflang alternates between EN and FR pages, with an x-default
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
