# Use the official Node.js 21 image as the base
FROM node:22-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Next.js app files to the container
COPY . .

# Build the Next.js app
RUN npm run build

# Expose the port on which the app will run (change it as per your Next.js configuration)
EXPOSE 3000

# Start the Next.js app
CMD ["npm", "start"]
