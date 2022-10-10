# Dockerfile for nextjs and nginx


## how to use these files
1. Copy all these files and folders and add to root of the nextjs project
2. Change the npm lock file based on yoor preference (`npm or yarn, default is yarn`)
3. use below commands to create and run the docker image

## Build images
- prerequisite is docker installed and running on local
```
docker-compose build
```

## Run images locally
- prerequisite is docker installed and running on local
```
docker-compose up -d
```
