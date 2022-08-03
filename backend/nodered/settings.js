module.exports = {
  credentialSecret: process.env.NODERED_PASSWORD,
  adminAuth: {
    type: "credentials",
    users: [
        {
            username: "tweecked",
            password: "$2a$08$McB46XnYSjVJWIN9Ynkno.1ntx8Qjh5vGsYHheTPuIgcp2hY.BfYi",
            permissions: "*"
        }
    ]
  }
}

