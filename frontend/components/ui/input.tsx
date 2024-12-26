// Import React with type information
import * as React from "react"
import { cn } from "@/lib/utils"

// Define our InputProps interface
// This extends HTML input element props to maintain full input functionality
export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {}

// Create the Input component using forwardRef to properly handle ref forwarding
// This is important for form libraries and accessibility
const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          // Base styles using the cn utility for class name merging
          "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2",
          "text-sm ring-offset-background",
          "file:border-0 file:bg-transparent file:text-sm file:font-medium",
          "placeholder:text-muted-foreground",
          "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
          "disabled:cursor-not-allowed disabled:opacity-50",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)

// Set a display name for better debugging in React DevTools
Input.displayName = "Input"

// Export the component both as default and named export
// This provides flexibility in how other files can import it
export { Input }
export default Input