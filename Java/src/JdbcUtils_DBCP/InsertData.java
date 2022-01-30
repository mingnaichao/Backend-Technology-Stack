package JdbcUtils_DBCP;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertData {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pst = null;

        try {
            conn = JdbcUtils_DBCP.getConnection(); // 获取数据库链接
            String sql = "insert into perf_assess_activity(name) values(?);";
            pst = conn.prepareStatement(sql);
            pst.setString(1, "20220130act");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils_DBCP.release(conn, pst, null); // 释放资源
        }
    }
}
