'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import Input from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { X } from 'lucide-react'

interface AddPaperFormProps {
  onClose: () => void
}

export default function AddPaperForm({ onClose }: AddPaperFormProps) {
  const [title, setTitle] = useState('')
  const [keywords, setKeywords] = useState('')
  const [abstract, setAbstract] = useState('')
  const [authors, setAuthors] = useState([''])
  const [date, setDate] = useState('')
  const [citations, setCitations] = useState('')
  const [url, setUrl] = useState('')

  const handleAuthorChange = (index: number, value: string) => {
    const newAuthors = [...authors]
    newAuthors[index] = value
    setAuthors(newAuthors)
  }

  const handleAddAuthor = () => {
    setAuthors([...authors, ''])
  }

  const handleRemoveAuthor = (index: number) => {
    if (authors.length > 1) {
      const newAuthors = authors.filter((_, i) => i !== index)
      setAuthors(newAuthors)
    }
  }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()

    // Validation
    if (authors.length === 0 || authors.some(author => author.trim() === '')) {
      alert('The paper must have at least one author.')
      return
    }

    if (abstract.split(' ').length < 10) {
      alert('The abstract should be at least 10 words.')
      return
    }

    const year = new Date(date).getFullYear()
    const paperData = { title, keywords, abstract, authors, year, citations, url }
    
    try {
      const response = await fetch('http://localhost:8000/add-paper', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(paperData),
      })
      const result = await response.json()
      console.log(result)
      onClose()
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <div 
      className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="bg-white/10 backdrop-blur-xl rounded-3xl p-6 w-full max-w-2xl relative my-8 max-h-[90vh] shadow-xl border border-white/20 overflow-y-auto custom-scrollbar">
        <Button
          variant="ghost"
          size="icon"
          className="absolute top-4 right-4"
          onClick={onClose}
        >
          <X className="h-4 w-4" />
        </Button>
        <h2 className="text-2xl font-bold mb-4 pt-8">Add New Paper</h2>
        <form onSubmit={handleSubmit} className="space-y-4 pr-2">
          <div>
            <label htmlFor="title" className="block text-sm font-medium mb-1">Title</label>
            <Input
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full bg-white/10 border-white/20"
              required
            />
          </div>
          <div>
            <label htmlFor="keywords" className="block text-sm font-medium mb-1">Keywords</label>
            <Input
              id="keywords"
              value={keywords}
              onChange={(e) => setKeywords(e.target.value)}
              className="w-full bg-white/10 border-white/20"
            />
          </div>
          <div>
            <label htmlFor="abstract" className="block text-sm font-medium mb-1">Abstract</label>
            <Textarea
              id="abstract"
              value={abstract}
              onChange={(e) => setAbstract(e.target.value)}
              className="w-full bg-white/10 border-white/20"
              rows={4}
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Authors</label>
            {authors.map((author, index) => (
              <div key={index} className="flex items-center space-x-2 mb-2">
                <Input
                  value={author}
                  onChange={(e) => handleAuthorChange(index, e.target.value)}
                  className="w-full bg-white/10 border-white/20"
                />
                {authors.length > 1 && (
                  <Button
                    variant="ghost"
                    size="icon"
                    onClick={() => handleRemoveAuthor(index)}
                    className="text-red-500 hover:text-red-700"
                  >
                    <X className="h-4 w-4" />
                  </Button>
                )}
              </div>
            ))}
            <Button
              type="button"
              onClick={handleAddAuthor}
              className="w-full bg-blue-500 text-white hover:bg-blue-700 mt-2"
            >
              Add Author
            </Button>
          </div>
          <div>
            <label htmlFor="date" className="block text-sm font-medium mb-1">Date</label>
            <Input
              id="date"
              type="date"
              value={date}
              onChange={(e) => setDate(e.target.value)}
              className="w-full bg-white/10 border-white/20"
            />
          </div>
          <div>
            <label htmlFor="citations" className="block text-sm font-medium mb-1">Citations</label>
            <Input
              id="citations"
              type="number"
              value={citations}
              onChange={(e) => setCitations(e.target.value)}
              className="w-full bg-white/10 border-white/20"
            />
          </div>
          <div>
            <label htmlFor="url" className="block text-sm font-medium mb-1">URL</label>
            <Input
              id="url"
              type="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              className="w-full bg-white/10 border-white/20"
            />
          </div>
          <Button
            type="submit"
            className="w-full bg-blue-500 text-white hover:bg-blue-700 mt-4"
          >
            Add Paper
          </Button>
        </form>
      </div>
    </div>
  )
}