#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')

# Outputs the matches
puts matches
