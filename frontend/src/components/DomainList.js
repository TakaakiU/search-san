// frontend/src/components/DomainList.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Linkをインポート
import apiClient from '../api';

const DomainList = () => {
  const [domains, setDomains] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newDomainUrl, setNewDomainUrl] = useState('');

  // ドメイン一覧を取得する関数
  const fetchDomains = async () => {
    try {
      setLoading(true);
      const response = await apiClient.get('/domains/');
      setDomains(response.data);
      setError(null);
    } catch (err) {
      setError('データの取得に失敗しました。');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // コンポーネントがマウントされた時に初回データを取得
  useEffect(() => {
    fetchDomains();
  }, []);

  // フォーム送信時の処理
  const handleSubmit = async (e) => {
    e.preventDefault(); // フォームのデフォルト送信動作をキャンセル
    if (!newDomainUrl.trim()) {
      alert('ドメインURLを入力してください。');
      return;
    }
    try {
      // APIにPOSTリクエストを送信
      await apiClient.post('/domains/', { url: newDomainUrl });
      setNewDomainUrl(''); // 入力フォームをクリア
      alert('ドメインが正常に登録されました。');
      fetchDomains(); // 登録後にドメイン一覧を再取得して画面を更新
    } catch (err) {
      // バックエンドからのバリデーションエラーなどを考慮
      if (err.response && err.response.data && err.response.data.url) {
        alert(`エラー: ${err.response.data.url[0]}`);
      } else {
        alert('ドメインの登録に失敗しました。');
      }
      console.error(err);
    }
  };

  if (loading) return <p>読み込み中...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      {/* 新規ドメイン登録フォーム */}
      <div className="domain-form">
        <h3>新しいドメインを登録</h3>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={newDomainUrl}
            onChange={(e) => setNewDomainUrl(e.target.value)}
            placeholder="example.com"
          />
          <button type="submit">登録</button>
        </form>
      </div>

      <h2>登録済みドメイン一覧</h2>
      {domains.length === 0 ? (
        <p>登録されているドメインはありません。</p>
      ) : (
        <ul>
          {domains.map((domain) => (
            <li key={domain.id}>
              <Link to={`/domains/${domain.id}/articles`}>
                {domain.url}
              </Link>
              (登録日: {new Date(domain.created_at).toLocaleDateString()})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default DomainList;