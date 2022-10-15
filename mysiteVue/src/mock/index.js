const Mock = require("mockjs");

let data = Mock.mock({
  "data|10": [ //生成6条数据 数组
    {
      "course_id|+1": 1,
      "course_name": "@title(10)", //生成商品信息，长度为10个汉字
      "course_teacher_name": "@cname",//生成商品名 ， 都是中国人的名字
      "course_info": /^1(5|3|7|8)[0-9]{9}$/,//生成随机电话号
      "course_time|1-1000": 1,
    }
  ]
})
Mock.mock('/delete', 'post', () => {
  return {error: 0}
})
Mock.mock('/add', 'post', () => {
  return {error: 0}
})
Mock.mock('/edit', 'post', () => {
  return {error: 0}
})

Mock.mock('/data', 'get', () => {
  return data
})
