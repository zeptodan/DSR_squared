"use client"

import { useState, useEffect, useRef } from "react"
import SearchBar from "@/components/SearchBar"
import SearchResults from "@/components/SearchResults"
import ScrollToTop from "@/components/ScrollToTop"
import AboutPopup from "@/components/AboutPopup"
import { Button } from "@/components/ui/button"
import { LayoutGrid, LayoutList, ArrowDownAZ, Calendar, QuoteIcon as Citation, InfoIcon } from "lucide-react"
import { logoFont } from "@/styles/fonts"

export default function Home() {
  const [query, setQuery] = useState("")
  const [searchKey, setSearchKey] = useState(0)
  const [isScrolled, setIsScrolled] = useState(false)
  const [isTwoColumns, setIsTwoColumns] = useState(false)
  const [sortBy, setSortBy] = useState("relevance")
  const [showAbout, setShowAbout] = useState(false)
  const mainRef = useRef<HTMLDivElement>(null)

  console.log("Initial state:", {
    query,
    searchKey,
    isScrolled,
    isTwoColumns,
    sortBy,
    showAbout,
  })

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 100)
    }

    window.addEventListener("scroll", handleScroll)
    return () => window.removeEventListener("scroll", handleScroll)
  }, [])

  const handleSearch = (newQuery: string) => {
    setQuery(newQuery.trim())
    setSearchKey((prevKey) => prevKey + 1) // Force a new search
    if (mainRef.current) {
      mainRef.current.scrollIntoView({ behavior: "smooth" })
    }
  }

  const buttonClasses =
    "bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors rounded-full border-2 border-white/50"

  return (
    <main ref={mainRef} className="min-h-screen smooth-gradient bg-gradient-to-br from-slate-800 to-black text-white">
      <div className={`transition-all duration-500 ease-in-out ${query ? "pt-8" : "pt-[30vh]"}`}>
        {query && isScrolled && (
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
          <div className="max-w-6xl mx-auto px-4 mt-8 pb-16">
            <div className="flex justify-between items-center w-full mb-4">
              <div className="flex items-center space-x-2">
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() =>
                    setSortBy(sortBy === "relevance" ? "date" : sortBy === "date" ? "citations" : "relevance")
                  }
                  className={buttonClasses}
                  title={`Ordered by ${sortBy}`}
                >
                  {sortBy === "relevance" ? (
                    <ArrowDownAZ className="h-4 w-4" />
                  ) : sortBy === "date" ? (
                    <Calendar className="h-4 w-4" />
                  ) : (
                    <Citation className="h-4 w-4" />
                  )}
                </Button>
              </div>
              <div className="flex items-center space-x-2">
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => setIsTwoColumns(false)}
                  className={`${buttonClasses} ${!isTwoColumns ? "bg-blue-500 text-white" : ""}`}
                  title="Single column view"
                >
                  <LayoutList className="h-4 w-4" />
                </Button>
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => setIsTwoColumns(true)}
                  className={`${buttonClasses} ${isTwoColumns ? "bg-blue-500 text-white" : ""}`}
                  title="Two column view"
                >
                  <LayoutGrid className="h-4 w-4" />
                </Button>
              </div>
            </div>
            <SearchResults key={searchKey} query={query} isTwoColumns={isTwoColumns} sortBy={sortBy} />
          </div>
        )}
      </div>
      <ScrollToTop />
      {showAbout && <AboutPopup onClose={() => setShowAbout(false)} />}
      {!query && (
        <div className="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-10">
          <Button
            variant="outline"
            size="lg"
            onClick={() => setShowAbout(true)}
            className="rounded-full px-6 py-2 text-sm font-medium bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors border-2 border-white/50"
          >
            <InfoIcon className="w-4 h-4 mr-2" />
            About
          </Button>
        </div>
      )}
    </main>
  )
}
