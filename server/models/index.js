const Influx = require('influx');
const config = require('../config/config')

const influx = new Influx.InfluxDB({
    host: config.database.host,
    port: config.database.port,
    protocol: config.database.protocol,
    username: config.database.username,
    password: config.database.password,
    database: 'home',
    schema: [
        {
            measurement: config.measurements.living_room_in.temperature,
            fields: {
                value: Influx.FieldType.FLOAT
            },
            tags: [
                'temperature',
                'in',
                'living_room'
            ]
        },
        {
            measurement: config.measurements.living_room_in.humidity,
            fields: {
                value: Influx.FieldType.FLOAT
            },
            tags: [
                'humidity',
                'in',
                'living_room'
            ]
        }
    ]
});

class Measurement {
    async insertMeasurements(measurements) {
        await influx.writePoints(measurements);
    }
}

module.exports = new Measurement();
