FROM node:14
WORKDIR /app
COPY package.json ./
RUN npm install --production
COPY . .
EXPOSE 8002
CMD ["node", "service2.js"]