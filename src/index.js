const request = require('request')
require('dotenv').config()

const access_token = process.env.ACCESS_TOKEN
console.log(access_token)

const URI = `https://openapi.band.us/v2.1/bands?access_token=${access_token}`
request(URI, function(error, response, body) {
  console.error('error:', error) // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode) // Print the response status code if a response was received
  console.log('body:', body) // Print the HTML for the Google homepage.
})
