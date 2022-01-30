package JdbcStudy;

import java.sql.*;

public class JdbcStudy {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 1.加载驱动（固定写法）
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 2.用户信息和url
        //useUnicode=ture&characterEncoding=utf8&useSSL=true
        String url = "jdbc:mysql://localhost:3306/8_0220?useUnicode=true$characterEncoding=utf8&useSSL=true";
        String username = "root";
        String password = "mnc0314?";

        // 3.链接数据库DriverManager，数据库对象 Connection 代表数据库
        Connection connection = DriverManager.getConnection(url, username, password);

        // 4.执行SQL对象 Statement 执行sql的对象
        Statement statement = connection.createStatement();

        // 5.执行SQL对象 执行SQL，可能存在结果，查看返回结果
        String sql1 = "select * from perf_assess_activity;";
        ResultSet resultSet = statement.executeQuery(sql1);

        /*
        statement.excute(sql); // 可以执行任何sql，但是效率低一点
        statement.excuteUpdate(sql); // 新增、编辑、删除都用这个，返回值为受影响的行数

        resultSet.getObject(field); // 不知道类型时使用
        resultSet.getString(field)；
        resultSet.getInt(field);
        resultSet.getFloat(field);
        resultSet.getDate(field);
         */

        while (resultSet.next()) {
            System.out.println("id=" + resultSet.getObject("id"));
            System.out.println("name=" + resultSet.getObject("name"));
            System.out.println("begin_date=" + resultSet.getObject("begin_date"));
            System.out.println("end_date=" + resultSet.getObject("end_date"));
            System.out.println("------");
        }
        // 6.释放链接
        resultSet.close();
        statement.close();
        connection.close();
    }
}
