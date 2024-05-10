#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/^\d{10,10}$/)

# Outputs the matches
puts matches
