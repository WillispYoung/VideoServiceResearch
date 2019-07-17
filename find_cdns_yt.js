// Note: Make sure to open Chrome's remote debugging port first!
// This file will search for the CDNs used in YouTube for several hundred web pages.

const CDP = require('chrome-remote-interface');
const fs = require('fs');

var domains = new Set();
var appended = new Set();

async function find_cdn(urls, index) {
	let client;

	if ((index + 1) % 40 == 0) {
		console.log("processed " + index.toString() + " urls.");
		appended.forEach(d => {
   			fs.appendFile(args[3], d + "\n", error => {});
		});
		appended.clear();
	}

	if (index >= urls.length) {
		// Save result.
		appended.forEach(d => {
   			fs.appendFile(args[3], d + "\n", error => {});
		});
		return;
	}

	url = urls[index];

	try {
		client = await CDP();
		const {Network, Page} = client;

		// CDN url is contained in params.request.url.
		Network.requestWillBeSent((params) => {
			words = params.request.url.split("/");
			if (words.length > 2) {
				domain = words[2];
				if (domain.endsWith("googlevideo.com")) {
					if (!domains.has(domain)) {
						domains.add(domain);
						appended.add(domain);
					}	
				}
			}
		});

		await Network.enable();
		await Page.enable();

		await Page.navigate({url: url});
		await Page.loadEventFired();
	}
	catch (err) {
		console.error(err);
	}
	finally {
		// Force synchronous execution.
		setTimeout(function() {
			find_cdn(urls, index + 1);
		}, 100);
	}
}

// node this.js url_file cdn_file
var args = process.argv;
var urls = fs.readFileSync(args[2]).toString().split('\n');

find_cdn(urls, 0);


// Break down record:
// 19-7-17 280; 320; pages