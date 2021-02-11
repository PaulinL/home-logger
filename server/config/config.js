
module.exports = {
    port: 3001,
    database: {
        host: process.env.INFLUXDB_HOST || 'localhost',
        port: process.env.INFLUXDB_PORT || 8086,
        protocol: 'http',
        username: process.env.INFLUXDB_USERNAME || 'admin',
        password: process.env.INFLUXDB_PASSWORD || 'admin',
        name: process.env.INFLUXDB_DB || 'home'
    },
    measurements: {
        living_room_in: {
            temperature: 'temperature_living_room_in',
            humidity: 'humidity_living_room_in'
        }
    }
}
