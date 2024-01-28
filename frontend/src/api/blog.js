import request from '@/utils/request'
// 文章：获取文章列表
export const getBlogListService = () => request.get('/blog/list')
// 文章：根据ID获取文章详情
export const getBlogIDService = (id) => request.get(`/blog/${id}`)
// 文章：根据ID修改文章 title-content
export const putBlogIDService = (id, title, content) =>
  request.put(`/blog/${id}`, { title, content })
// 文章：新建文章
export const postBlogService = (title, content) =>
  request.post('/blog', { title, content })
