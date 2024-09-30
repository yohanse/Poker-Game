import {test, expect} from "@playwright/test";

test.describe("API Request Tests", () => {
    test("Get action method", async({request}) => {
        const response = await request.post("http://localhost:8000/game/start?stack=122");
        expect(response.status()).toBe(200);
        
        const text = await response.text();
        const keys: string[] = ["id", "setup", "status", "pot", "hole_cards"];
        keys.forEach(element => expect(text).toContain(element));
        
    });
});