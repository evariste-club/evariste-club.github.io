var ptx_lunr_search_style = "textbook";
var ptx_lunr_docs = [
{
  "id": "prosort",
  "level": "1",
  "url": "prosort.html",
  "type": "Section",
  "number": "1",
  "title": "Prosort Euler",
  "body": " Prosort Euler   An event we're doing with FooBar for ESYA'25    My First Subsection  Some more words  foo   A frog   A nice-looking frog with a longish description.    Bar:   "
},
{
  "id": "subsection-1-4",
  "level": "2",
  "url": "prosort.html#subsection-1-4",
  "type": "Figure",
  "number": "1.1",
  "title": "",
  "body": " A frog   A nice-looking frog with a longish description.   "
},
{
  "id": "pwnhub",
  "level": "1",
  "url": "pwnhub.html",
  "type": "Section",
  "number": "2",
  "title": "PWNHUB",
  "body": " PWNHUB  CTF's we started organizing.   Ellie  Our very first box! The goal was to familiarize myself and others with the basic infrastructure, ssh 'ing into a box and using simple commands to retrieve a flag.    Benjamin  Our second box! This time, we aimed to delve deeper into the system, exploring user permissions and file structures to uncover the flag.   bar  "
}
]

var ptx_lunr_idx = lunr(function () {
  this.ref('id')
  this.field('title')
  this.field('body')
  this.metadataWhitelist = ['position']

  ptx_lunr_docs.forEach(function (doc) {
    this.add(doc)
  }, this)
})
