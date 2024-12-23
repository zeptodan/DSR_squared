'use client'

import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { ChevronLeft, ChevronRight } from 'lucide-react'

interface SearchResult {
  id: number
  title: string
  description: string
  authors: string[]
  date: string
  citations: number
  doi: string
}

interface SearchResultsProps {
  query: string
  isTwoColumns: boolean
  sortBy: string
}

export default function SearchResults({ query, isTwoColumns, sortBy }: SearchResultsProps) {
  const [results, setResults] = useState<SearchResult[]>([])
  const [currentPage, setCurrentPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const resultsPerPage = 10

  const generateResults = (page: number, count: number) => {
    const startIndex = (page - 1) * count + 1
    return Array.from({ length: count }, (_, i) => ({
      id: startIndex + i,
      title: `Research on ${query}: Implications for DSR² Technology (Result ${startIndex + i})`,
      description: `This groundbreaking research explores the applications of ${query} in the context of DSR² technology. The study provides valuable insights into improving search algorithms and user experience.`,
      authors: ['John Doe', 'Jane Smith', 'Alice Johnson'],
      date: `202${Math.floor(Math.random() * 4)}-${String(Math.floor(Math.random() * 12) + 1).padStart(2, '0')}-${String(Math.floor(Math.random() * 28) + 1).padStart(2, '0')}`,
      citations: Math.floor(Math.random() * 1000),
      doi: `10.1000/dsr2.${Math.random().toString(36).substr(2, 8)}`
    }))
  }

  useEffect(() => {
    if (query) {
      const newResults = generateResults(currentPage, resultsPerPage)
      setResults(newResults)
      setTotalPages(5) // Simulating 5 pages of results
    } else {
      setResults([])
      setTotalPages(1)
    }
  }, [query, currentPage, sortBy])

  useEffect(() => {
    setCurrentPage(1)
  }, [query, sortBy])

  useEffect(() => {
    if (sortBy === 'date') {
      setResults(prev => [...prev].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()))
    } else {
      setResults(prev => [...prev].sort((a, b) => b.citations - a.citations))
    }
  }, [sortBy])

  const handlePageChange = (newPage: number) => {
    setCurrentPage(newPage)
  }

  if (!query) return null

  return (
    <div>
      <div className={`grid gap-4 sm:gap-6 ${isTwoColumns ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1'}`}>
        {results.map((result) => (
          <div key={result.id} className="p-4 sm:p-6 rounded-md bg-white/10 backdrop-blur-md hover:bg-white/15 transition-colors">
            <h2 className="text-lg sm:text-xl font-semibold mb-2 group">
              <a href="#" className="text-white group-hover:text-blue-500 transition-colors">
                <span className="bg-left-bottom bg-gradient-to-r from-blue-500 to-blue-500 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-300 ease-out">
                  {result.title}
                </span>
              </a>
            </h2>
            <p className="text-gray-300 mb-4">{result.description}</p>
            <div className="flex flex-wrap gap-4 text-sm text-gray-400">
              <div>Authors: {result.authors.join(', ')}</div>
              <div>Published: {result.date}</div>
              <div>Citations: {result.citations}</div>
              <div>DOI: {result.doi}</div>
            </div>
          </div>
        ))}
      </div>
      <div className="flex justify-center items-center mt-8 space-x-2">
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className="rounded-full bg-white/10 backdrop-blur-md text-white hover:bg-blue-500 hover:text-white transition-colors border-2"
        >
          <ChevronLeft className="h-4 w-4" />
        </Button>
        {Array.from({ length: totalPages }, (_, i) => i + 1).map((page) => (
          <Button
            key={page}
            variant={page === currentPage ? "default" : "outline"}
            onClick={() => handlePageChange(page)}
            className={`rounded-full w-10 h-10 ${
              page === currentPage
                ? 'bg-blue-500 text-white'
                : 'bg-white/10 backdrop-blur-md text-white hover:bg-blue-500 hover:text-white border-2'
            } transition-colors`}
          >
            {page}
          </Button>
        ))}
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className="rounded-full bg-white/10 backdrop-blur-md text-white hover:bg-blue-500 hover:text-white transition-colors border-2"
        >
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  )
}

