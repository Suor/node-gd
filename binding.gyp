{
  "targets": [
    {
      "target_name": "node-gd",
      "sources": ["node-gd.cc"],
      "libraries": ["-lgd"],
      "conditions": [
          [ 'OS=="freebsd"', {
            "libraries": ["-L/usr/local/lib"],
            "include_dirs": ["/usr/local/include"],
          }]
      ]
    }
  ]
}
