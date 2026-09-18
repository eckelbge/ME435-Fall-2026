classdef MyShape < handle

    properties
        Patch matlab.graphics.primitive.Patch
    end

    methods
        function obj = MyShape(xCords,yCords,color)
            obj.Patch = patch(xCords,yCords,color);
        end

        function move(obj, dx, dy)
            obj.Patch.XData=obj.Patch.XData + dx;
            obj.Patch.YData=obj.Patch.YData + dy;
        end
    end
end