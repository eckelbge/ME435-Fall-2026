classdef Exam1LED

    properties
        Property1
    end

    methods
        function obj = Exam1LED(unusedComPort)
            fprintf('Connected\n');
        end
        function response = sendCommand(obj, command)
            import matlab.net.*
            import matlab.net.http.*

            r = RequestMessage;
            uri = URI("http://137.112.199.90:5000/api/" + command);
            resp = send(r,uri);
            response = resp.Body.Data;
            fprintf("Response to %s --> %s", command, response);           
        end
    end
end