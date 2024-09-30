FROM mcr.microsoft.com/playwright:focal

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npx playwright install chromium

CMD ["npx", "playwright", "test"]