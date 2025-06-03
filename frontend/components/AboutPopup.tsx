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

        <div className="pt-8 pb-6">
          <h2 className="text-3xl font-bold mb-6 text-center">
            About DSR<span className="text-blue-500">²</span>
          </h2>

          <div className="space-y-4 text-gray-100">
            <p>
              DSR² (Delectable Succulent Research Retrieval) is a modern search engine designed specifically for
              academic and scientific research papers. Our mission is to make scientific knowledge more accessible,
              searchable, and interconnected.
            </p>

            <p>
              Using advanced natural language processing and semantic search technologies, DSR² helps researchers find
              relevant papers more efficiently than traditional keyword-based search engines.
            </p>

            <p>Key features include:</p>

            <ul className="list-disc pl-6 space-y-2">
              <li>Semantic search that understands the meaning behind your queries</li>
              <li>Citation network analysis to discover related research</li>
              <li>Filtering by publication date, citation count, and more</li>
              <li>Clean, distraction-free reading experience</li>
              <li>Personalized recommendations based on your research interests</li>
            </ul>

            <p>
              DSR² is currently in beta. We're constantly improving our algorithms and adding new features based on user
              feedback. If you have suggestions or encounter any issues, please reach out to us through one of the
              channels below.
            </p>
          </div>
        </div>

        <div className="border-t border-white/20 pt-6">
          <h3 className="text-xl font-semibold mb-4 text-center">Connect With Us</h3>

          <div className="flex flex-wrap justify-center gap-3">
            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("https://linkedin.com", "_blank")}
            >
              <Linkedin className="h-4 w-4 mr-2" />
              LinkedIn
            </Button>

            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("https://github.com", "_blank")}
            >
              <Github className="h-4 w-4 mr-2" />
              GitHub
            </Button>

            <Button
              variant="outline"
              className="bg-white/10 hover:bg-blue-500 hover:text-white transition-colors border-white/30 rounded-full"
              onClick={() => window.open("mailto:contact@dsr2.com")}
            >
              <Mail className="h-4 w-4 mr-2" />
              Email
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}
