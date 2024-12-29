'use client';

import { useState, useEffect, useCallback, useRef } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronLeft, ChevronRight, ChevronsLeft, ChevronsRight } from 'lucide-react';

interface SearchResult {
  id: number;
  title: string;
  description: string;
  authors: string[];
  date: string;
  citations: number;
  url: string;
}

interface SearchResultsProps {
  query: string;
  isTwoColumns: boolean;
  sortBy: string;
}

export default function SearchResults({ query, isTwoColumns, sortBy }: SearchResultsProps) {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [totalResults, setTotalResults] = useState(0);
  const [searchTime, setSearchTime] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const isFetching = useRef(false);
  const _resultsPerPage = 10;

  console.log('Initial state:', {
    results,
    currentPage,
    totalPages,
    totalResults,
    searchTime,
    error,
  });

  const fetchResults = useCallback(async (page: number) => {
    if (isFetching.current) return; // Prevent multiple fetch requests
    isFetching.current = true;
    setError(null);
    try {
      console.log('Fetching results for query:', query, 'page:', page);

      const response = await fetch(
        `http://localhost:8000/search?query=${encodeURIComponent(query)}&page=${page}`
      );
      if (!response.ok) {
        throw new Error('Failed to fetch results');
      }
      const data = await response.json();
      console.log('Fetched data:', data);

      setResults(data.results);
      setTotalPages(data.total_pages);
      setTotalResults(data.total_results);
      setSearchTime(data.search_time);
    } catch (err) {
      setError('An error occurred while fetching results. Please try again.');
      console.error(err);
    } finally {
      isFetching.current = false;
    }
  }, [query]);

  useEffect(() => {
    if (query) {
      fetchResults(currentPage);
    } else {
      setResults([]);
      setTotalPages(1);
      setTotalResults(0);
      setSearchTime(0);
    }
  }, [query, currentPage, fetchResults]);

  useEffect(() => {
    setCurrentPage(1);
  }, [query]);

  const sortedResults = [...results].sort((a, b) => {
    if (sortBy === 'date') {
      return new Date(b.date).getTime() - new Date(a.date).getTime();
    } else if (sortBy === 'citations') {
      return b.citations - a.citations;
    }
    return 0; // 'relevance' or default order
  });

  const handlePageChange = (newPage: number) => {
    console.log('Changing page to:', newPage);
    if (newPage > 0 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
  };

  const highlightText = (text: string, highlight: string) => {
    if (!highlight.trim()) {
      return text;
    }
    const regex = new RegExp(`(${highlight})`, 'gi');
    return text.split(regex).map((part, index) =>
      regex.test(part) ? <span key={index} className="bg-yellow-300">{part}</span> : part
    );
  };

  if (!query) return null;

  const buttonClasses =
    'bg-white/20 backdrop-blur-md hover:bg-blue-500 hover:text-white transition-colors rounded-full border-2 border-white/50';

  const startPage = Math.max(1, currentPage - 2);
  const endPage = Math.min(totalPages, currentPage + 2);
  const pages = Array.from({ length: endPage - startPage + 1 }, (_, i) => startPage + i);

  return (
    <div>
      {error && <div className="text-red-500 mb-4">{error}</div>}
      <div className="text-sm text-gray-400 mb-4">
        {totalResults} results returned in {searchTime.toFixed(4)} seconds
      </div>
      <div
        className={`grid gap-4 sm:gap-6 ${isTwoColumns ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1'}`}
      >
        {sortedResults.map((result) => (
          <div
            key={result.id}
            className="p-4 sm:p-6 rounded-md bg-white/10 backdrop-blur-md hover:bg-white/15 transition-colors"
          >
            <h2 className="text-lg sm:text-xl font-semibold mb-2 group">
              <a
                href={result.url}
                target='_blank'
                className="text-white group-hover:text-blue-500 transition-colors"
              >
                <span className="bg-left-bottom bg-gradient-to-r from-blue-500 to-blue-500 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-300 ease-out">
                  {highlightText(result.title, query)}
                </span>
              </a>
            </h2>
            <p className="text-gray-300 mb-4 line-clamp-3">{highlightText(result.description, query)}</p>
            <div className="flex flex-wrap gap-4 text-sm text-gray-400">
              <div>Authors: {result.authors.join(', ')}</div>
              <div>Published: {result.date}</div>
              <div>Citations: {result.citations}</div>
            </div>
          </div>
        ))}
      </div>
      <div className="flex justify-center items-center mt-8 space-x-2">
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(1)}
          disabled={currentPage === 1}
          className={buttonClasses}
        >
          <ChevronsLeft className="h-4 w-4" />
        </Button>
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1}
          className={buttonClasses}
        >
          <ChevronLeft className="h-4 w-4" />
        </Button>
        {pages.map((page) => (
          <Button
            key={page}
            variant={page === currentPage ? 'default' : 'outline'}
            onClick={() => handlePageChange(page)}
            className={`rounded-full w-10 h-10 ${
              page === currentPage
                ? 'bg-blue-500 text-white border-2 border-blue-500'
                : buttonClasses
            }`}
          >
            {page}
          </Button>
        ))}
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={currentPage === totalPages}
          className={buttonClasses}
        >
          <ChevronRight className="h-4 w-4" />
        </Button>
        <Button
          variant="outline"
          size="icon"
          onClick={() => handlePageChange(totalPages)}
          disabled={currentPage === totalPages}
          className={buttonClasses}
        >
          <ChevronsRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}