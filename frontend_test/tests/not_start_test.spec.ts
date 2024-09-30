import { test, expect } from '@playwright/test';

test("Shouldn't start with invalid stack", async({page}) => {
    await page.goto('http://localhost:3000');
    await page.getByPlaceholder('stack').fill("-1000");
    await page.getByRole('button', { name: 'start' }).click();
    const response: string | null= await page.locator('.bg-white').textContent();
    console.log(response);
    expect(response).toBe("");
  });