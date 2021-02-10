
module.exports = {
    port: 3001,
    database: {
        host: process.env.INFLUXDB_HOST,
        port: process.env.INFLUXDB_PORT,
        protocol: 'http',
        username: process.env.INFLUXDB_USERNAME,
        password: process.env.INFLUXDB_PASSWORD
    },
    measurements: {
        living_room_in: {
            temperature: 'temperature_living_room_in',
            humidity: 'humidity_living_room_in'
        }
    }
}
