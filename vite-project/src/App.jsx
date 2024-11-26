import { CreateJournalPage } from './pages/CreateJournalPage'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/create-journal" element={<CreateJournalPage />} />
        <Route path="/journals" element={<CreateJournalPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
