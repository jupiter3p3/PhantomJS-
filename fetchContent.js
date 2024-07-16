var page = require('webpage').create();
var system = require('system');
var url = system.args[1];

page.open(url, function(status) {
    if (status !== 'success') {
        console.log('Unable to access the network');
        phantom.exit();
    } else {
        var content = page.content;
        console.log(content);
        phantom.exit();
    }
});
