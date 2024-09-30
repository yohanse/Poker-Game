import { test, expect } from '@playwright/test';

test('should start successfully with valid stack', async ({ page }) => {
    await page.goto('http://localhost:3000');
    await page.getByPlaceholder('stack').fill("1000");
    await page.getByRole('button', { name: 'start' }).click();
    const response: string | null = await page.locator('.bg-white').textContent();
    
    for(var i=0; i<6; i++){
        expect(response).toContain(`Player ${i + 1} is dealt`);
    }
    });