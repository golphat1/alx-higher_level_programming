#!/usr/bin/node

const request = require('request');

// Check the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Send GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const tasks = JSON.parse(body);

      // Create object to store the completed tasks count for each user
      const completedTasksByUser = {};

      // Iterate through the tasks and count completed tasks for each user
      for (const task of tasks) {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      }

      // Prints a completed tasks count by user
      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
