import { useState,useEffect,useRef } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
// Pages
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Contact } from './pages/Contact'
import { Sounds } from './pages/Sounds'
import { Signin } from './pages/Signin'
import { Signup } from './pages/Signup'
import { Blog } from './pages/Blog'

// Components
import NavBar from './components/Nav'
import { Footer } from './components/Footer'


import './App.css'

function App(){


  return (
    <div className="App h-full">
      {/* ใช้ Routes แล้วเลือก path ได้ */}
      <BrowserRouter>
       
        <NavBar />
      
          <Routes>
            //Setting with 'path="/"' on First Webpage
            <Route path="/" element={<Home />} />

            <Route path="/home" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/sounds" element={<Sounds />} />
            <Route path="/signin" element={<Signin />} />
            <Route path="/blog" element={<Blog />} />
            {/* <Route path="/signup" element={<Signup />} /> */}
          </Routes>

        <Footer/>
        
      </BrowserRouter>
      
    </div>
  )
}


export default App