#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/^h[a-zA-Z0-9]n$/)

# Outputs the matches
puts matches
