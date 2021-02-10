const express = require('express');
const router = express.Router();
const Measurements = require('../../models');

module.exports = () => {
    router.post('/', async (req, res) => {
        console.log(req.body);
        try {
            await Measurements.insertMeasurements(req.body.measurements);
            res.sendStatus(200);
        } catch (err) {
            console.log(err)
            res.sendStatus(401);
        }
    });

    return router;
};
