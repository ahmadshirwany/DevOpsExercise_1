const express = require('express');
const {execSync} = require('child_process');
const axios = require('axios');
const app = express();
const PORT = 8002;

function get_uptime() {
    const uptime_s = parseFloat(execSync('cat /proc/uptime | awk \'{print $1}\'').toString());
    const uptime_h = uptime_s / 3600;
    const freespace_in_kb = parseInt(execSync('df / | tail -1 | awk \'{print $4}\'').toString());
    const freespace_in_mb = freespace_in_kb / 1024;
    const time = new Date().toISOString().replace('T', ' ').replace('Z', '');
    return `Timestamp2 : Uptime: ${uptime_h} hours, Free Memory: ${freespace_in_mb} MB, Time: ${time}`;
}
app.get('/status', async (req, res) => {
    const data = get_uptime();
    try {
        await axios.post('http://storage:8003/log', data, { 
            headers: {'Content-Type': 'text/plain'} 
        });
        console.log('Successfully sent data to storage service');
    } catch (error) {
        console.error('Error sending data to storage service:', error.message);
    } 

    try {
        const fs = require('fs');
        const logDir = '/vstorage';
        if (!fs.existsSync(logDir)) {
            fs.mkdirSync(logDir, { recursive: true });
        }
        fs.appendFileSync('/vstorage/log.txt', data + '\n\n');
    } catch (error) {
        console.error('Error writing to local log file:', error.message);
    }
    
    res.set('Content-Type', 'text/plain');
    res.send(data);
});

app.listen(PORT, () => { console.log(`Service2 running on port ${PORT}`); });

