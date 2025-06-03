"use client"

import type React from "react"

import { useState, useEffect } from "react"
import { Search } from "lucide-react"

interface SearchBarProps {
  onSearch: (query: string) => void
  initialQuery: string
}

export default function SearchBar({ onSearch, initialQuery }: SearchBarProps) {
  const [query, setQuery] = useState(initialQuery)

  console.log("Initial state:", {
    query,
  })

  useEffect(() => {
    setQuery(initialQuery)
  }, [initialQuery])

  const handleSearch = (e: React.FormEvent) => {
    console.log("Search is pressed")
    e.preventDefault()
    console.log("handleSearch called with query:", query)
    onSearch(query)
  }

  return (
    <form onSubmit={handleSearch} className="relative w-full mx-auto">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
        className="w-full p-3 sm:p-4 pr-12 rounded-full bg-white/20 backdrop-blur-md border-2 border-white/50 focus:outline-none focus:ring-1 focus:ring-blue-400 focus:border-blue-400 transition-all placeholder:text-white/70 text-white"
      />
      <button
        type="submit"
        className="absolute right-2 top-1/2 -translate-y-1/2 bg-blue-500 hover:bg-blue-600 rounded-full p-2 transition-colors border-1 border-blue-500 hover:border-blue-600"
      >
        <Search className="w-5 h-5 text-white" />
      </button>
    </form>
  )
}
