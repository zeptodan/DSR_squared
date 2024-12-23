'use client'

import { useState, useEffect, useRef } from 'react'
import SearchBar from '@/components/SearchBar'
import SearchResults from '@/components/SearchResults'
import ScrollToTop from '@/components/ScrollToTop'
import { Button } from '@/components/ui/button'
import { LayoutGrid, LayoutList, SortAsc } from 'lucide-react'
import { logoFont } from '@/styles/fonts'

export default function Home() {
  const [query, setQuery] = useState('')
  const [isScrolled, setIsScrolled] = useState(false)
  const [isTwoColumns, setIsTwoColumns] = useState(false)
  const [sortBy, setSortBy] = useState('relevance')
  const mainRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 100)
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const handleSearch = (newQuery: string) => {
    setQuery(newQuery)
    if (mainRef.current) {
      mainRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <main ref={mainRef} className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white">
      <div className={`transition-all duration-500 ease-in-out ${query ? 'pt-8' : 'pt-[30vh]'}`}>
        {(query && isScrolled) && (
          <div className="sticky top-4 z-10 w-[calc(100%-2rem)] sm:w-[calc(100%-4rem)] md:w-[calc(100%-8rem)] lg:w-[90%] xl:w-[95%] max-w-[1600px] mx-auto">
            <div className="bg-white/20 backdrop-blur-lg rounded-3xl shadow-lg transition-all duration-500 ease-in-out py-4 px-6">
              <h1 className={`${logoFont.className} text-3xl sm:text-4xl font-bold text-center mb-4`}>
                DSR<span className="text-blue-500">²</span>
              </h1>
              <SearchBar onSearch={handleSearch} initialQuery={query} />
            </div>
          </div>
        )}
        {(!isScrolled || !query) && (
          <div className="max-w-3xl mx-auto px-4">
            <h1 className={`${logoFont.className} text-6xl font-bold text-center mb-8`}>
              DSR<span className="text-blue-500">²</span>
            </h1>
            <SearchBar onSearch={handleSearch} initialQuery={query} />
          </div>
        )}
        {query && (
          <div className="max-w-6xl mx-auto px-4 mt-8">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-4">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setSortBy(sortBy === 'relevance' ? 'date' : 'relevance')}
                className="bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors w-full sm:w-auto rounded-full"
              >
                <SortAsc className="h-4 w-4 mr-2" />
                Sort by: {sortBy === 'relevance' ? 'Relevance' : 'Date'}
              </Button>
              <div className="hidden sm:flex items-center space-x-2">
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => setIsTwoColumns(false)}
                  className={`bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors rounded-full ${!isTwoColumns ? 'bg-blue-500 text-white' : ''}`}
                >
                  <LayoutList className="h-4 w-4" />
                </Button>
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => setIsTwoColumns(true)}
                  className={`bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors rounded-full ${isTwoColumns ? 'bg-blue-500 text-white' : ''}`}
                >
                  <LayoutGrid className="h-4 w-4" />
                </Button>
              </div>
            </div>
            <SearchResults query={query} isTwoColumns={isTwoColumns} sortBy={sortBy} />
          </div>
        )}
      </div>
      <ScrollToTop />
    </main>
  )
}

