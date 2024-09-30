import {test, expect} from "@playwright/test";

test('Continue after starting the game', async ({ page }) => {
      await page.pause();
      await page.goto('http://localhost:3000');
      await page.getByPlaceholder('stack').fill("1000");
      await page.getByRole('button', { name: 'start' }).click();
      const response: string | null = await page.locator('.bg-white').textContent({ timeout: 10000 });
      
      for(var i=0; i<6; i++){
          expect(response).toContain(`Player ${i + 1} is dealt`);
      }
  
      for(var i=0; i<5; i++) {
          await page.getByRole('button', { name: 'Fold' }).click()
      }
      console.log(response);
      const playerResponse: string | null = await page.locator('.bg-white').textContent();
      for(var i=0; i<5; i++) {
          const index = (i + 2) % 6 + 1
          expect(playerResponse).toContain(`Player ${index} folds`);
      }
  });