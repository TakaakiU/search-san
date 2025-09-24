import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import apiClient from '../api';

const ArticleListPage = () => {
  const { domainId } = useParams(); // URLからdomainIdを取得
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        setLoading(true);
        const response = await apiClient.get(`/articles/?domain=${domainId}`);
        setArticles(response.data);
        setError(null);
      } catch (err) {
        setError('記事データの取得に失敗しました。');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchArticles();
  }, [domainId]); // domainIdが変わるたびにデータを再取得

  if (loading) return <p>記事を読み込み中...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      <Link to="/">&larr; ドメイン一覧に戻る</Link>
      <h2>記事一覧 (ドメインID: {domainId})</h2>
      {articles.length === 0 ? (
        <p>この記事に紐づく記事はありません。</p>
      ) : (
        <ul>
          {articles.map((article) => (
            <li key={article.id}>{article.title || article.url}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ArticleListPage;
