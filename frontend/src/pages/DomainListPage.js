// frontend/src/pages/DomainListPage.js
import React from 'react';
import { Link } from 'react-router-dom';
import DomainList from '../components/DomainList'; // DomainListコンポーネントを再利用（後で修正）

const DomainListPage = () => {
  return (
    <div>
      {/* このページにドメイン一覧と登録フォームを配置 */}
      <DomainList /> 
    </div>
  );
};

export default DomainListPage;
