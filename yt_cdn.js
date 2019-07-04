// Note: Make sure to open Chrome's remote debugging port first!
// This file will search for the CDNs used in YouTube for several hundred web pages.

const CDP = require('chrome-remote-interface');
const fs = require('fs');

var domains = new Set();

async function find_cdn(urls, index) {
	let client;

	if (index >= urls.length) {
		// Save result.
		domains.forEach(d => {
   			fs.appendFile('yt_cdns.txt', d + "\n", error => {});
   			// console.log(d);
		});
		return;
	}

	url = urls[index];

	try {
		client = await CDP();
		const {Network, Page} = client;

		// CDN url is contained in params.request.url.
		Network.requestWillBeSent((params) => {
			// console.log("RS: " + params.request.url + "\n");
			words = params.request.url.split("/");
			if (words.length > 2) {
				domain = words[2];
				// console.log(domain);
				if (domain.endsWith("googlevideo.com")) {
					if (bad_cdns.has(domain)) {
						console.log("Hit bad CDN.");
					}
					// console.log(domain);
					domains.add(domain);
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
		// console.log(domains.size);
		find_cdn(urls, index + 1);
	}
}

var urls = fs.readFileSync('data/yt_urls.txt').toString().split('\n');
var bad_cdns = new Set();

var lines = fs.readFileSync('data/Singapore/yt_good_bad_cdns.txt').toString().split('\n');
var flag = false;

lines.forEach(line => {
	if (flag) {
		words = line.split(' ');
		if (words[0].length > 0) 
			bad_cdns.add(words[0]);
	}
	if (line.startsWith("Bad CDNs")) {
		flag = true;
	}
});

console.log(bad_cdns);

find_cdn(urls, 0);
