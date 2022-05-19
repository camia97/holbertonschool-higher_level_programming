#!/usr/bin/node
const axios = require('axios').default;
try {
  axios.get(process.argv[2]).then(function (response) {
    console.log('code:', response.status);
  });
} catch (error) {
  console.error(error);
}
