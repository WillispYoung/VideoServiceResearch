const CDP = require('chrome-remote-interface');
const fs = require('fs');

async function find_cdn(urls, index /* add pattern maybe ? */) {
	var client = await CDP();
	const {Network, Page} = client;

	var domains = {};
	var tmp_domain_set = new Set();

	// Capture certain Network information.
	Network.requestWillBeSent((params) => {
		words = params.request.url.split("/");
		if (words.length > 2) {
			domain = words[2];
			if (domain.endsWith("googlevideo.com")) {
				if (!tmp_domain_set.has(domain)) {
					console.log(count.toString() + " : " + domain);
					tmp_domain_set.add(domain);

					if (domain in domains)
						domains[domain] += 1;
					else
						domains[domain] = 1;
				}
			}
		}
	});

	// Iterate over certain amount of URLs synchronously.
	var url = urls[index];
	var count = 0;

	while (index < urls.length) {
		try {
			await Network.enable();
			await Page.enable();

			await Page.navigate({url: url});
			await Page.loadEventFired();
		}
		catch (error) {
			// console.error(error);
			console.log("Capture over.")
		}
		finally {
			count += 1;
			index += 1;

			if (/*count >= 400 ||*/ index >= urls.length) break;

			url = urls[index];
			tmp_domain_set.clear();

			setTimeout(d => {}, 1000);
		}
	}

	client.close();

	console.log(Object.keys(domains).length.toString() + " domains are captured.");

	// Save result.
	for (var key in domains) {
		fs.appendFile(args[3], key + " " + domains[key].toString() + "\n", error => {});
	}
}

// Command: node this_js urls cdns

var index = 0;
var args = process.argv;
var urls = fs.readFileSync(args[2]).toString().split('\n');

find_cdn(urls, index);

// Note: don't open right panel to "disable cache", 
// which would slow down the program instead.

// Q: Why CDNs used in previous video page appears in current one?
// I suppose this is because that socket in previous page is not closed, 
// yet a new page is opened, so that socket is counted into the new page.

// Q: Why CDNs used all seems work perfectly fine?
// Try higher video qualities.

// YouTube (July_4th -1, July_3rd): 144p (lowest)
// YouTube (July_4th -2): auto (mainly 720p+)
