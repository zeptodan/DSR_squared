'use client'

import { useState, useEffect } from 'react'
import { Search } from 'lucide-react'

interface SearchBarProps {
  onSearch: (query: string) => void
  initialQuery: string
}

export default function SearchBar({ onSearch, initialQuery }: SearchBarProps) {
  const [query, setQuery] = useState(initialQuery)

  console.log('Initial state:', {
    query,
  })

  useEffect(() => {
    setQuery(initialQuery)
  }, [initialQuery])

  const handleSearch = (e: React.FormEvent) => {
    console.log("Search is pressed")
    e.preventDefault()
    console.log('handleSearch called with query:', query)
    onSearch(query)
  }

  return (
    <form onSubmit={handleSearch} className="relative w-full mx-auto">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
        className="w-full p-3 sm:p-4 pr-12 rounded-full bg-white/10 backdrop-blur-md focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all"
      />
      <button
        type="submit"
        className="absolute right-2 top-1/2 -translate-y-1/2 bg-blue-500 rounded-full p-2 hover:bg-blue-600 transition-colors"
      >
        <Search className="w-5 h-5" />
      </button>
    </form>
  )
}