# Test task for Numbers

This application parses Google Sheet. Creds for Google Sheet API are already exists in repository

# Installation

Clone repository to your machine

`git clone https://github.com/slaveeks/test-task `

`cd test-task`

## Configuration

You need to configure app

1. To configure postgreSQL database you need to rename `./.env.sample` file
to `.env` and set your values
2. To configure service you need to rename `./service/.env.sample` file
to `.env` and set your values, also you need to get telegram bot token from @BotFather
3. To configure api you need to rename `./api/.env.sample` file
to `.env` and set your values

## Before running app

Before you run, you need to send some message to your bot to get notifications

## How to run

You need to have a Docker to run app

Firstly, you need to build app:

`docker-compose build`

Secondly, you need to run it:

`docker-compose up`

Then you can see app on `http://localhost:3000/`



