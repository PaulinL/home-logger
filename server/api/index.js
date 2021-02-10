const express = require('express');
const measurement = require('./routes/measurement')

const router = express.Router();


module.exports = () => {
    router.use('/measurement', measurement());

    return router;
}
