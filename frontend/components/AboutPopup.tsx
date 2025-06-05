"use client"

import { useEffect } from "react"
import { Button } from "@/components/ui/button"
import { X, Linkedin, Github, Mail } from "lucide-react"

interface AboutPopupProps {
  onClose: () => void
}

export default function AboutPopup({ onClose }: AboutPopupProps) {
  // Prevent scrolling of the background when popup is open
  useEffect(() => {
    document.body.style.overflow = "hidden"
    return () => {
      document.body.style.overflow = "auto"
    }
  }, [])

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 backdrop-blur-md"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose()
      }}
    >
      <div className="bg-white/10 backdrop-blur-xl rounded-3xl p-6 w-full max-w-2xl relative my-8 max-h-[90vh] shadow-xl border border-white/20 overflow-y-auto custom-scrollbar">
        <Button variant="ghost" size="icon" className="absolute top-4 right-4 hover:bg-white/20" onClick={onClose}>
          <X className="h-4 w-4" />
        </Button>

        <div className="pt-6 pb-6">
          <h2 className="text-3xl font-bold mb-6 text-center">
            About DSR<span className="text-blue-500">²</span>
          </h2>

          <div className="space-y-4 text-gray-100">
            <p>
              DSR² (Delectable Succulent Research Retrieval) (yes) is a search engine based on a 
              corpus of 1 million+ academic and research papers. Using natural language processing 
              and semantic search technologies, DSR² helps users find relevant papers efficiently.
            </p>

            <p>Key features include:</p>

            <ul className="list-disc pl-6 space-y-2">
              <li>Clean, modern UI</li>
              <li>Query expansion with semantic search</li>
              <li>Filtering by publication date, citation count, and more</li>
            </ul>

            <p>
              If you'd like to know how DSR² was built, or would like to talk 
              to us about anything really, follow one of the links below.
            </p>
          </div>
        </div>

        <div className="border-t border-white/20 pt-6">
          <h3 className="text-xl font-semibold mb-4 text-center">Connect With Us</h3>

          <div className="flex flex-wrap justify-center gap-3 mb-6">
            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("https://www.linkedin.com/in/danish-munib/", "_blank")}
            >
              <Linkedin className="h-4 w-4 mr-2" />
              LinkedIn
            </Button>

            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("https://github.com/zeptodan/DSR_squareds", "_blank")}
            >
              <Github className="h-4 w-4 mr-2" />
              GitHub
            </Button>

            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("mailto:danishmunibcontact@gmail.com")}
            >
              <Mail className="h-4 w-4 mr-2" />
              Email
            </Button>
          </div>

          <div className="space-y-4 text-gray-100 text-sm">
            <p className="text-center text-gray-400 pt-4 border-t border-white/20">
               DSR² is a proof-of-concept. One of the creators is working on a much improved 
               version from the ground up, and will be updating about it as developments happen.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
