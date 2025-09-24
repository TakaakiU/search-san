// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
// import DomainList from './components/DomainList';
import DomainListPage from './pages/DomainListPage';
import ArticleListPage from './pages/ArticleListPage';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          {/* ロゴとプロジェクト名を表示 */}
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Search San</h1>
        </header>
        
        {/* メインコンテンツエリア */}
        <main className="App-content">
          <Routes>
            <Route path="/" element={<DomainListPage />} />
            <Route path="/domains/:domainId/articles" element={<ArticleListPage />} />
          </Routes>
        </main>

        {/* フッター（任意） */}
        <footer className="App-footer">
          <p>Your SERP Tracking Tool</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;