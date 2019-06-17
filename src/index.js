require('dotenv').config()
const rp = require('request-promise')

const access_token = process.env.ACCESS_TOKEN
const band_key = process.env.BAND_KEY_DEV
const content = `
밴드 글 입력 테스트
`

// const URI = `https://openapi.band.us/v2.1/bands`

// const options = {
//   uri: 'https://openapi.band.us/v2.1/bands',
//   qs: {
//     access_token,
//     band_key,
//     content
//   },
//   headers: {
//     'User-Agent': 'Request-Promise'
//   },
//   json: true // Automatically parses the JSON string in the response
// }

const options = {
  method: 'POST',
  uri: 'https://openapi.band.us/v2.2/band/post/create',
  body: {
    access_token,
    band_key,
    content
  },
  json: true // Automatically stringifies the body to JSON
}

rp(options)
  .then(res => {
    // console.log('User has %d repos', res.length)
    console.log(res)
  })
  .catch(err => {
    // API call failed...
    console.log(err)
  })
