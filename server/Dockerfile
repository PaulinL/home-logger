FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3001

CMD [ "node", "index.js" ]
