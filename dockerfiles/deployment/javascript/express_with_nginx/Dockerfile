# Use the official Node.js 21 image as the base
FROM node:21-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Express.js app files to the container
COPY . .

# Expose the port on which the app will run (change it as per your Express.js configuration)
EXPOSE 3000

# Install PM2 globally
RUN npm install -g pm2

# Start the Express.js app with PM2
CMD ["pm2-runtime", "npm", "--", "start"]
